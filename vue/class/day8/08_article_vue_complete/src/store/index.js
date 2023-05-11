import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
// import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    article_id : 1,
    articles: [
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article){
      state.articles.push(article)
      state.article_id = state.article_id + 1
    },
    DELETE_ARTICLE(state, id){
      state.articles = state.articles.filter((article)=>{
        return !(article.id===id)
      })
    }
  },
  actions: {
    createArticle(context, payload){
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit('CREATE_ARTICLE', article) 
    }
  },
  modules: {
  }
})
