
  <template>
    <div class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-4xl font-extrabold text-gray-900 text-center mb-8">
          <span class="text-indigo-600">OrgAssist AI </span>
          <span>Metrics</span>
        </h2>
        
        <div v-if="loading" class="flex justify-center items-center h-64">
          <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-indigo-500"></div>
        </div>
        
        <div v-else-if="error" class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-8" role="alert">
          <p class="font-bold">Error</p>
          <p>{{ error }}</p>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(value, key) in data" :key="key" 
               class="bg-white rounded-xl shadow-lg overflow-hidden transform transition duration-500 hover:scale-105">
            <div class="p-6">
              <div class="flex justify-between items-center mb-4">
                <h3 class="text-lg font-semibold text-gray-900 flex items-center">
                  <component :is="getMetricIcon(key)" class="w-6 h-6 mr-2 text-indigo-600" />
                  {{ formatMetricName(key) }}
                </h3>
                <span class="text-2xl font-bold text-indigo-600">{{ formatValue(value) }}</span>
              </div>
              <div v-if="shouldShowPieChart(key)" class="flex justify-center mb-4">
                <svg class="w-32 h-32">
                  <circle cx="64" cy="64" r="60" fill="transparent" stroke="#E0E7FF" stroke-width="8" />
                  <circle cx="64" cy="64" r="60" fill="transparent" stroke="#4F46E5" stroke-width="8"
                          :stroke-dasharray="2 * Math.PI * 60"
                          :stroke-dashoffset="2 * Math.PI * 60 * (1 - value)"
                          transform="rotate(-90 64 64)"
                          class="transition-all duration-1000 ease-out" />
                </svg>
              </div>
              <div v-else class="relative pt-1 mb-4">
                <div class="overflow-hidden h-2 text-xs flex rounded bg-indigo-200">
                  <div :style="{ width: `${value * 100}%` }" 
                       class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500 transition-all duration-500 ease-out">
                  </div>
                </div>
              </div>
              <p class="text-sm text-gray-600">{{ getMetricDescription(key) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { 
    CheckCircleIcon, 
    ChatBubbleBottomCenterTextIcon, 
    MagnifyingGlassIcon, 
    DocumentTextIcon, 
    ExclamationTriangleIcon, 
    AcademicCapIcon 
  } from '@heroicons/vue/24/outline';
  
  const data = ref({});
  const loading = ref(true);
  const error = ref(null);
  
  const formatMetricName = (name) => {
    return name.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  };
  
  const formatValue = (value) => {
    return (value * 100).toFixed(1) + '%';
  };
  
  const getMetricDescription = (metric) => {
    const descriptions = {
      faithfulness: "This measures the factual consistency of the generated answer against the given context, with the score scaled from 0 to 1 (higher is better). Faithfulness is determined by checking if all claims in the answer can be inferred from the provided context.",
      answer_relevancy: "The Answer Relevancy metric assesses how relevant the generated answer is to the given prompt, with higher scores indicating better relevancy. It is computed using the question, context, and answer, and is defined as the mean cosine similarity of the original question to artificially generated questions based on the answer.",
      context_precision: "Context Precision evaluates if all relevant items in the contexts are ranked higher, ideally appearing at the top. It is computed using the question, ground-truth, and contexts, with values ranging from 0 to 1, where higher scores indicate better precision.",
      context_recall: "Context Recall measures how well the retrieved context aligns with the ground truth answer, with values ranging from 0 to 1 (higher is better). It is computed using the question, ground truth, and retrieved context by checking if claims in the ground truth can be attributed to the retrieved context. Ideally, all claims should align",
      harmfulness: "Does the submission cause or have the potential to cause harm to individuals, groups, or society at large? and Absence of harmful content (lower is better)",
      answer_correctness: "Answer Correctness gauges the accuracy of the generated answer compared to the ground truth, with scores ranging from 0 to 1 (higher scores indicating better alignment). It considers semantic and factual similarity, combined using a weighted scheme to form the correctness score."
    };
    return descriptions[metric] || "Performance metric";
  };
  
  const getMetricIcon = (metric) => {
    const icons = {
      faithfulness: CheckCircleIcon,
      answer_relevancy: ChatBubbleBottomCenterTextIcon,
      context_precision: MagnifyingGlassIcon,
      context_recall: DocumentTextIcon,
      harmfulness: ExclamationTriangleIcon,
      answer_correctness: AcademicCapIcon
    };
    return icons[metric] || CheckCircleIcon;
  };
  
  const shouldShowPieChart = (metric) => {
    return ['faithfulness', 'answer_relevancy', 'answer_correctness'].includes(metric);
  };
  
  onMounted(async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/evaluation");
      data.value = response.data.result;
    } catch (e) {
      console.error(e);
      error.value = "Failed to load evaluation data. Please try again later.";
    } finally {
      loading.value = false;
    }
  });
  </script>