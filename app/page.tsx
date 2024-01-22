
"use client"
import { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import { useUser } from '@auth0/nextjs-auth0/client';

export default function Home() {

    const { user } = useUser();
    const [data, setData] = useState({ cecum: [], feces: [], ileum: [] });
    const [projectIds, setProjectIds] = useState([]);
    const [selectedProjectId, setSelectedProjectId] = useState('');
    const [accessToken, setAccessToken] = useState(); 
    const [tokenObtenido, setTokenObtenido] = useState(false);
  
    useEffect(() => {
      const fetchToken = async () => {
        try {
          const response = await fetch('http://localhost:3000/api/authc/token', {
           
          });
          const { accessToken } = await response.json();
          setAccessToken(accessToken);
          setTokenObtenido(true);
        } catch (error) {
          console.error('Error al obtener token:', error);
        }
      };
  

  
      const fetchProjectIds = async () => {
        try {
          const response = await fetch('http://localhost:3000/api/projectid', {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          });
          if (!response.ok) {
            throw new Error('Respuesta no válida al obtener projectIds');
          }
          const result = await response.json();
          const ids = result.data
          setProjectIds(ids);
          if (ids && ids.length > 0) {
            setSelectedProjectId(ids[0]); // Establece el selectedProjectId aquí
            fetchData();
          }
         
        } catch (error) {
          console.error('Error al obtener projectIds:', error);
        }
      };
  
      fetchToken();
      if (tokenObtenido) {
      fetchProjectIds();}
    }, [tokenObtenido]);
  
    useEffect(() => {
      if (projectIds.length > 0) {
        setSelectedProjectId(projectIds[0]);
        console.log(selectedProjectId)
      }
    }, [projectIds]);
   

    useEffect(() => {
      if (selectedProjectId) {
        fetchData();
      }
    }, [selectedProjectId]);

const fetchData = async () => {
    try {
      const response = await fetch(`http://localhost:3000/api/featurecount/${selectedProjectId}`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        throw new Error('Respuesta no válida de la API');
      }

      const resp = await response.json();
      const newData = groupByAlphaShannon(resp.data);
      setData(newData);
    } catch (error) {
      console.error('Error al obtener datos:', error);
    }
  };

  function groupByAlphaShannon(data:any) {
    const groups = { cecum: [], feces: [], ileum: [] };
    data.forEach(item => {
      switch (item.sampleLocation) {
        case 'cecum':
          groups.cecum.push(item.alphaShannon);
          break;
        case 'feces':
          groups.feces.push(item.alphaShannon);
          break;
        case 'ileum':
          groups.ileum.push(item.alphaShannon);
          break;
        // Agrega otros casos si es necesario
        default:
          break;
      }
    });
    return groups;
  }

  const handleProjectIdChange = (event:any) => {
    setSelectedProjectId(event.target.value);
  };
  
console.log(projectIds)
  return (
    user && (
      <>
        <div>
          <h2>{user.name}</h2>
          <p>{user.email}</p>
        </div>
        {/* Menú desplegable para seleccionar projectId */}
        <div>
        <label htmlFor="project-select">Seleccione un Proyecto:</label>
        <select id="project-select" value={selectedProjectId} onChange={handleProjectIdChange}>
          {projectIds.map((project:any) => (
            <option key={project.projectId} value={project.projectId}>
              {project.projectId}
            </option>
          ))}
        </select>
      </div>
        <div>
          <h1>Diversity</h1>
          <BoxPlot data={data} />
        </div>
      </>
    )
  );
}

function BoxPlot({ data }:any) {
  const datagroup = [
    {
      y: data.cecum,
      type: 'box',
      name: 'Cecum'
    },
    {
      y: data.feces,
      type: 'box',
      name: 'Feces'
    },
    {
      y: data.ileum,
      type: 'box',
      name: 'Ileum'
    }
  ];

  return (
    <div>
      <Plot
        data={datagroup}
        layout={{ width: 720, height: 440, title: 'Alpha Shannon Diversity' }}
      />
    </div>
  );
}