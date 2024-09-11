<!-- <template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 sm:text-5xl md:text-6xl">
            About <span class="text-indigo-600">OrgAssist AI</span>
          </h1>
          <p class="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Learn more about our AI-powered HR policy assistant and how it can revolutionize your organization.
          </p>
        </div>
  
        <div class="mt-10">
          <div class="prose prose-lg max-w-3xl mx-auto text-gray-500">
            <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Mission</h2>
            <p>
              At OrgAssist AI, our mission is to simplify and streamline HR processes by providing instant, accurate answers to policy questions. We believe that by empowering employees with easy access to information, we can create more efficient and harmonious workplaces.
            </p>
  
            <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">How It Works</h2>
            <p>
              OrgAssist AI utilizes advanced natural language processing to understand and respond to your HR policy questions. Our AI is trained on a comprehensive database of HR policies and best practices, ensuring that you receive the most up-to-date and relevant information.
            </p>
  
            <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">Key Features</h2>
            <ul class="list-disc pl-6">
              <li>24/7 availability for instant policy information</li>
              <li>Continuous learning and updates to stay current with policy changes</li>
              <li>Natural language understanding for easy, conversational interactions</li>
              <li>Customizable to your organization's specific policies and procedures</li>
            </ul>
  
            <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">Get Started</h2>
            <p>
              Ready to transform your HR experience? Start chatting with OrgAssist AI today and discover how easy managing HR policies can be.
            </p>
            <div class="mt-8">
              <router-link
                to="/model"
                class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-150 ease-in-out"
              >
                Try OrgAssist AI
                <svg class="ml-2 -mr-1 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  // No additional setup needed for this component
  </script> -->

<!-- 
  <template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-5xl font-bold text-gray-900 sm:text-6xl md:text-7xl mb-4">
            About <span class="text-indigo-600 animate-pulse">OrgAssist AI</span>
          </h1>
          <p class="mt-3 max-w-md mx-auto text-xl text-gray-600 sm:text-2xl md:mt-5 md:max-w-3xl">
            Revolutionizing HR with AI-powered insights
          </p>
        </div>
  
        <div class="mt-10 grid gap-10 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(feature, index) in features" :key="index" 
               class="bg-white rounded-xl shadow-lg overflow-hidden transform transition duration-500 hover:scale-105"
               :class="{'md:col-span-2': index === features.length - 1 && features.length % 2 !== 0}">
            <div class="p-8">
              <div class="flex items-center justify-center w-16 h-16 bg-indigo-100 text-indigo-500 rounded-full mb-4">
                <component :is="feature.icon" class="h-8 w-8" />
              </div>
              <h3 class="text-2xl font-semibold text-gray-900 mb-2">{{ feature.title }}</h3>
              <p class="text-gray-600">{{ feature.description }}</p>
            </div>
          </div>
        </div>
  
        <div class="mt-16">
          <h2 class="text-3xl font-bold text-center text-gray-900 mb-8">How OrgAssist AI Works</h2>
          <div class="relative">
            <div class="absolute inset-0 flex items-center" aria-hidden="true">
              <div class="w-full border-t border-gray-300"></div>
            </div>
            <div class="relative flex justify-between">
              <span v-for="step in workflowSteps" :key="step.id" 
                    class="bg-indigo-600 text-white px-4 py-2 rounded-full text-sm font-medium transform transition duration-500 hover:scale-110">
                {{ step.name }}
              </span>
            </div>
          </div>
        </div>
  
        <div class="mt-16 text-center">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Ready to Transform Your HR Experience?</h2>
          <p class="text-xl text-gray-600 mb-8">Start chatting with OrgAssist AI today and discover how easy managing HR policies can be.</p>
          <router-link
            to="/model"
            class="inline-flex items-center px-8 py-3 border border-transparent text-lg font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110"
          >
            Try OrgAssist AI
            <svg class="ml-2 -mr-1 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { BoltIcon, ClockIcon, ChatBubbleBottomCenterTextIcon, ShieldCheckIcon, ArrowPathIcon } from '@heroicons/vue/24/outline';
  
  const features = ref([
    {
      icon: BoltIcon,
      title: 'Instant Answers',
      description: 'Get immediate responses to your HR policy questions, saving time and reducing uncertainty.'
    },
    {
      icon: ClockIcon,
      title: '24/7 Availability',
      description: "Access HR information anytime, anywhere, ensuring you're always informed about company policies."
    },
    {
      icon: ChatBubbleBottomCenterTextIcon,
      title: 'Natural Conversations',
      description: 'Interact with our AI using natural language, just like chatting with a human HR expert.'
    },
    {
      icon: ShieldCheckIcon,
      title: 'Up-to-Date Policies',
      description: 'Our AI is constantly updated with the latest HR policies and procedures.'
    },
    {
      icon: ArrowPathIcon,
      title: 'Continuous Learning',
      description: 'OrgAssist AI improves over time, learning from interactions to provide even better assistance.'
    },
  ]);
  
  const workflowSteps = ref([
    { id: 1, name: 'Ask a Question' },
    { id: 2, name: 'AI Processes' },
    { id: 3, name: 'Retrieve Information' },
    { id: 4, name: 'Provide Answer' },
    { id: 5, name: 'Continuous Improvement' },
  ]);
  </script> -->

  <template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-5xl font-bold text-gray-900 sm:text-6xl md:text-7xl mb-4">
            AI-Powered <span class="text-indigo-600">HR Solutions</span>
          </h1>
          <p class="mt-3 max-w-md mx-auto text-xl text-gray-600 sm:text-2xl md:mt-5 md:max-w-3xl">
            Revolutionizing human resources with cutting-edge artificial intelligence
          </p>
        </div>
  
        <div class="mt-10 bg-white shadow-xl rounded-lg overflow-hidden">
          <div class="p-8">
            <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Technology</h2>
            <p class="text-gray-600 mb-6">
              OrgAssist AI leverages state-of-the-art natural language processing and machine learning algorithms to understand and respond to HR queries with unprecedented accuracy and speed. Our AI model is trained on vast amounts of HR data, policies, and best practices, enabling it to provide contextually relevant and up-to-date information.
            </p>
            <h2 class="text-3xl font-bold text-gray-900 mb-4">Key Benefits</h2>
            <ul class="list-disc list-inside text-gray-600 mb-6">
              <li>Instant access to HR information, 24/7</li>
              <li>Reduced workload for HR departments</li>
              <li>Consistent and accurate policy interpretation</li>
              <li>Scalable solution for organizations of all sizes</li>
              <li>Continuous learning and improvement</li>
            </ul>
          </div>
        </div>
  
        <div class="mt-16">
          <h2 class="text-3xl font-bold text-center text-gray-900 mb-8">How OrgAssist AI Works</h2>
          <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
            <div v-for="(step, index) in workflowSteps" :key="index" class="bg-white p-6 rounded-lg shadow-md">
              <div class="text-indigo-600 text-4xl font-bold mb-2">{{ index + 1 }}</div>
              <h3 class="text-xl font-semibold text-gray-800 mb-2">{{ step.title }}</h3>
              <p class="text-gray-600">{{ step.description }}</p>
            </div>
          </div>
        </div>
  
        <div class="mt-16 text-center">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Experience AI-Driven HR Excellence</h2>
          <p class="text-xl text-gray-600 mb-8">Streamline your HR processes with OrgAssist AI today.</p>
          <router-link
            to="/model"
            class="inline-flex items-center px-8 py-3 border border-transparent text-lg font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110"
          >
            Try OrgAssist AI
            <svg class="ml-2 -mr-1 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const workflowSteps = ref([
    {
      title: "Query Input",
      description: "Users input their HR-related questions in natural language."
    },
    {
      title: "AI Processing",
      description: "Our advanced AI analyzes the query and understands the context."
    },
    {
      title: "Knowledge Retrieval",
      description: "Relevant information is retrieved from our comprehensive HR database."
    },
    {
      title: "Response Generation",
      description: "A clear, accurate answer is generated and delivered to the user."
    }
  ]);
  </script>