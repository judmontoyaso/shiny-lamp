"use client"
import { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import React from 'react';
import { useUser } from '@auth0/nextjs-auth0/client';
import { getAccessToken, withApiAuthRequired } from '@auth0/nextjs-auth0';

export default function Home() {

  const { user, error, isLoading } = useUser();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>{error.message}</div>;
//   interface DataItem {
  interface DataItem {
    sampleLocation: string;
    alphaShannon: number;
}
interface Data {
  cecum: number[];  
  feces: number[];
  ileum: number[];
  // Add other properties as needed
}

const [data, setData] = useState<Data>({
  cecum: [],
  feces: [],
  ileum: [],
  // Initialize other properties as needed
});

const fetchData = async () => {

    const tokenResponse = await fetch('/api/authc/token');
    if (!tokenResponse.ok) {
      throw new Error('No se pudo obtener el token de acceso');
    }else{"consulta de token realizada"}
    console.log(tokenResponse)
    const { accessToken } = await tokenResponse.json();
    console.log(accessToken)
    // Realizar la solicitud a tu API FastAPI con el token


    const response = await fetch('http://localhost:3000/api/featurecount/E349', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (!response.ok) {
      throw new Error('Respuesta no válida de la API');
    }



  const data: DataItem[] = await response.json();
console.log(data)
  function groupByAlphaShannon(data: DataItem[]) {
      const groups: Data = {
          cecum: [],
          feces: [],
          ileum: [],
      };

      data.forEach((item: DataItem) => {
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
              // Add other cases if needed
              default:
                  break;
          }
      });

      return groups;
  }

  const groupedData = groupByAlphaShannon(data);
  setData(groupedData);
};


useEffect(() => {
  fetchData();
}, []);
   

  

  const BoxPlot = () => {

  
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
      

      {/* <Plot
      data={datagroup}
      layout={{ width: 720, height: 440, title: 'Alpha Shannon E355' }}
      /> */}
    </div>
  );
  };
  

  

  return (
    user && (
      <>
      <div>
        <h2>{user.name}</h2>
        <p>{user.email}</p>
      </div>
<div>
      <h1>Diversity</h1>
      <BoxPlot />
    </div>
      </>
  ))}
