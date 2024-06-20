<template>
    <div>
      <h1>Communicating from an Arduino to Node.js</h1>
      <div id="sample" :style="sampleStyle">
        {{ data }}%
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  import { io } from 'socket.io-client';
  
  const data = ref('');
  const sampleStyle = {
    backgroundColor: 'red',
    width: '300px',
    height: '300px',
  };
  
  onMounted(() => {
    console.log("Mounting component and attempting to connect to socket...");
    const socket = io('http://localhost:3000', {
      withCredentials: false
    }); // 确保这里的URL和端口与你的Node.js服务器匹配
  
    socket.on('connect', () => {
      console.log('Successfully connected to the socket server.');
    });
  
    socket.on('connect_error', (error) => {
      console.error('Connection failed:', error);
    });
  
    socket.on('data', newData => {
      console.log(`New data received: ${newData}`);
      data.value = newData;
    });
  
    onUnmounted(() => {
      console.log("Component is unmounting, disconnecting socket...");
      socket.off('data');
      socket.disconnect();
    });
  });
  </script>