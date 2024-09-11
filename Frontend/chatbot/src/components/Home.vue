<!-- <template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-4">
            <span class="text-indigo-600">OrgAssist AI</span>
          </h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Get instant answers to your HR policy questions. Our AI-powered chatbot is here to help you navigate company policies with ease.
          </p>
        </div>
  
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center mb-16">
          <div class="order-2 md:order-1">
            <h2 class="text-3xl font-bold text-gray-900 mb-4">Empower Your HR Journey</h2>
            <p class="text-lg text-gray-600 mb-6">
              Our OrgAssist AI is designed to make your work life easier. With instant access to company policies and procedures, you'll never be left in the dark.
            </p>
            <router-link 
              to="/model" 
              class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-150 ease-in-out"
            >
              Start Chatting
              <svg class="ml-2 -mr-1 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </router-link>
          </div>
          <div class="order-1 md:order-2">
            <img :src="image" alt="HR Policy" class="rounded-lg shadow-xl">
          </div>
        </div>
  
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <FeatureCard 
            icon="M13 10V3L4 14h7v7l9-11h-7z" 
            title="Quick Answers" 
            description="Get instant responses to your HR policy questions, saving time and reducing uncertainty."
          />
          <FeatureCard 
            icon="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" 
            title="Always Up-to-Date" 
            description="Our chatbot is constantly updated with the latest HR policies and procedures."
          />
          <FeatureCard 
            icon="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm12 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z" 
            title="24/7 Availability" 
            description="Access HR information anytime, anywhere, ensuring you're always informed about company policies."
          />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import FeatureCard from './FeatureCard.vue';

  import image from '../components/image.png'
  import real from "../assets/real.png"
  </script> -->


  <template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="text-center mb-16">
          <h1 class="text-5xl md:text-7xl font-bold text-gray-900 mb-4">
            <span class="text-indigo-600 animate-pulse">OrgAssist AI</span>
          </h1>
          <p class="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto">
            Get instant answers to your HR policy questions. Our AI-powered chatbot is here to help you navigate company policies with ease.
          </p>
        </div>
  
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-16">
          <div class="order-2 md:order-1 space-y-6">
            <h2 class="text-4xl font-bold text-gray-900">Empower Your HR Journey</h2>
            <p class="text-xl text-gray-600">
              Our OrgAssist AI is designed to make your work life easier. With instant access to company policies and procedures, you'll never be left in the dark.
            </p>
            <router-link 
              to="/model" 
              class="inline-flex items-center px-8 py-3 border border-transparent text-lg font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110"
            >
              Start Chatting
              <svg class="ml-2 -mr-1 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </router-link>
          </div>
          <div class="order-1 md:order-2 transform transition duration-500 hover:scale-105">
            <img :src="image" alt="HR Policy" class="rounded-lg shadow-2xl">
          </div>
        </div>
  
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="(feature, index) in features" :key="index" 
               class="bg-white rounded-xl shadow-lg overflow-hidden transform transition duration-500 hover:scale-105">
            <div class="p-8">
              <div class="flex items-center justify-center w-16 h-16 bg-indigo-100 text-indigo-500 rounded-full mb-4">
                <component :is="feature.icon" class="h-8 w-8" />
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ feature.title }}</h3>
              <p class="text-gray-600">{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { BoltIcon, ClockIcon, ChatBubbleBottomCenterTextIcon } from '@heroicons/vue/24/outline';
  
  import image from '../components/image.png'
  
  const features = ref([
    {
      icon: BoltIcon,
      title: "Quick Answers",
      description: "Get instant responses to your HR policy questions, saving time and reducing uncertainty."
    },
    {
      icon: ClockIcon,
      title: "24/7 Availability",
      description: "Access HR information anytime, anywhere, ensuring you're always informed about company policies."
    },
    {
      icon: ChatBubbleBottomCenterTextIcon,
      title: "Natural Conversations",
      description: "Interact with our AI using natural language, just like chatting with a human HR expert."
    }
  ]);
  </script>