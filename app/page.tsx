"use client"
import { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import React from 'react';

export default function Home() {
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
  const response = await fetch('http://localhost:3000/api/featureCount/E355');
  const data: DataItem[] = await response.json();

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
  
  // return (
  // <Plot
  // data={datagroup}
  // layout={{ width: 720, height: 440, title: 'Alpha Shannon E355' }}
  // />
  // );
  };
  

  

  return (
<div>
      {/* <h1>Diversity</h1>
      <BoxPlot /> */}
    </div>
  );
}
