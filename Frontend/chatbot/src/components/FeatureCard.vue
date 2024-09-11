<template>
    <div class="bg-white rounded-xl shadow-lg overflow-hidden transform transition duration-500 hover:scale-105">
      <div class="p-8">
        <div class="flex items-center justify-center w-16 h-16 bg-indigo-100 text-indigo-500 rounded-full mb-4">
          <svg class="h-8 w-8" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="icon" />
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ title }}</h3>
        <p class="text-gray-600">{{ description }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    icon: String,
    title: String,
    description: String
  });
  </script>