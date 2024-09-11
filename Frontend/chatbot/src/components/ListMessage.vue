
<template>
    <div>
      <div v-for="item in ChatHistory.ChatHistory" :key="item.id" :class="[
        'mb-4 p-3 rounded-lg',
        item.sender === 'User' ? 'bg-blue-100 text-right' : 'bg-gray-200'
      ]">
        <p class="font-semibold mb-1">{{ item.sender }}</p>
        <p>{{ item.text }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '../stores/Index';
  
  const ChatHistory = useCounterStore();
  </script>

