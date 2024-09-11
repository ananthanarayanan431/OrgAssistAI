
import { defineStore } from "pinia";

export const useCounterStore = defineStore('Chatmessage',{
    state: ()=> ({
        History:[{id:Date.now(),text: "Hello, I'm OrgAssistAI",sender:'Assistant'},]
    }),
    actions:{
        addMessage(message){
            this.History.push(message)
        },
        ClearMessage() {
            this.History.splice(1,this.History.length)
        },
    },

    getters:{
        ChatHistory: (state)=> {
            return state.History
        },
    },
})