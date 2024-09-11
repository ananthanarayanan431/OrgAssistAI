<!-- <template>
    <div class="min-h-screen bg-gray-100 p-4">
      <div class="max-w-3xl mx-auto bg-white rounded-lg shadow-md p-6">
        <h2 class="text-2xl font-bold mb-4">OrgAssist AI</h2>
        <div class="mb-4 h-96 overflow-y-auto bg-gray-50 p-4 rounded">
          <ListMessage />
        </div>
        <form @submit.prevent="askQuestion" class="flex gap-2">
          <input 
            type="text" 
            v-model="question" 
            placeholder="Ask a question" 
            required 
            :disabled="loading"
            class="flex-grow p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
          <button 
            type="submit" 
            :disabled="loading || !question.trim()"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 disabled:opacity-50"
          >
            {{ loading ? 'Generating...' : 'Send' }}
          </button>
          <button 
            @click.prevent="ChatHistory.ClearMessage"
            :disabled="loading"
            class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300 disabled:opacity-50"
          >
            Clear
          </button>
        </form>
      </div>
    </div>
</template>
  
  <script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useCounterStore } from '../stores/Index';
  import ListMessage from './ListMessage.vue';
  
  const question = ref('')
  const ChatHistory = useCounterStore()
  const loading = ref(false)
  
  const askQuestion = async () => {
    if (!question.value.trim()) return;
    
    loading.value = true
    try {
      ChatHistory.addMessage({ id: Date.now(), text: question.value, sender: 'User' })
      const response = await axios.post("http://127.0.0.1:8000/model", { question: question.value })

      ChatHistory.addMessage({ id: Date.now() + 1, text: response.data.result, sender: 'Assistant' });
      console.log("Message Sent!")
    } catch (error) {
      console.error("Error in Generating", error);

      let errorMessage = "Sorry, an error occurred. Please try again.";
      if (error.response && error.response.status === 500) {
        errorMessage += " The server encountered an internal error.";
      }
      ChatHistory.addMessage({ id: Date.now() + 1, text: errorMessage, sender: 'Assistant' })
    } finally {
      question.value = "";
      loading.value = false;
    }
  }
  </script> -->


  <template>
    <div class="h-screen flex flex-col bg-gray-100">
      <!-- Header -->
      <!-- <header class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
          <h1 class="text-2xl font-semibold text-gray-900">OrgAssist AI Chat</h1>
        </div>
      </header> -->
  
      <!-- Chat area -->
      <div class="flex-grow overflow-hidden flex flex-col">
        <!-- Messages -->
        <div class="flex-grow overflow-y-auto p-4 space-y-4" ref="chatContainer">
          <div v-for="item in ChatHistory.ChatHistory" :key="item.id" 
               :class="[
                 'max-w-3xl mx-auto p-4 rounded-lg shadow',
                 item.sender === 'User' ? 'bg-indigo-100 ml-auto' : 'bg-white mr-auto'
               ]">
            <p class="font-semibold mb-1">{{ item.sender }}</p>
            <p>{{ item.text }}</p>
          </div>
        </div>
  
        <!-- Input area -->
        <div class="bg-white border-t border-gray-200 p-4">
          <form @submit.prevent="askQuestion" class="max-w-3xl mx-auto flex gap-4">
            <input 
              type="text" 
              v-model="question" 
              placeholder="Ask a question about HR policies..." 
              required 
              :disabled="loading"
              class="flex-grow p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
            <button 
              type="submit" 
              :disabled="loading || !question.trim()"
              class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 disabled:opacity-50"
            >
              {{ loading ? 'Thinking...' : 'Ask' }}
            </button>
            <button 
              @click.prevent="ChatHistory.ClearMessage"
              :disabled="loading"
              class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 disabled:opacity-50"
            >
              Clear
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted, watch } from 'vue';
  import { useCounterStore } from '../stores/Index';
  
  const question = ref('')
  const ChatHistory = useCounterStore()
  const loading = ref(false)
  const chatContainer = ref(null)
  
  const askQuestion = async () => {
    if (!question.value.trim()) return;
    
    loading.value = true
    try {
      ChatHistory.addMessage({ id: Date.now(), text: question.value, sender: 'User' })
      const response = await axios.post("http://127.0.0.1:8000/model", { question: question.value })
  
      ChatHistory.addMessage({ id: Date.now() + 1, text: response.data.result, sender: 'Assistant' });
      console.log("Message Sent!")
    } catch (error) {
      console.error("Error in Generating", error);
  
      let errorMessage = "Sorry, an error occurred. Please try again.";
      if (error.response && error.response.status === 500) {
        errorMessage += " The server encountered an internal error.";
      }
      ChatHistory.addMessage({ id: Date.now() + 1, text: errorMessage, sender: 'Assistant' })
    } finally {
      question.value = "";
      loading.value = false;
    }
  }
  
  // Scroll to bottom when new messages are added
  // watch(() => ChatHistory.ChatHistory.length, () => {
  //   setTimeout(() => {
  //     if (chatContainer.value) {
  //       chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  //     }
  //   }, 0)
  // })
  
  // Initial scroll to bottom
  // onMounted(() => {
  //   if (chatContainer.value) {
  //     chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  //   }
  // })
  </script>