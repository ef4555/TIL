import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
    doubleNumber: 0
  },
  getters: {
  },
  mutations: {
    CHANGE_NUMBER(state, payload) {
      state.counter = payload
    }
  },
  actions: {
    changeNumber(context, newNumber) {
      context.commit('CHANGE_NUMBER', newNumber)
    },
  },
  modules: {
  }
})
