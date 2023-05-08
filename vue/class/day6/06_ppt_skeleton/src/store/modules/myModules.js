const myModule = {
  state: {
    level: 20,
  },
  mutations: {
    INCREMENT_level(state) {
      state.level += 1
    }
  },
  actions: {
    increment_level(constext) {
      constext.commit('INCREMENT_level')
    }
  },
}

export default myModule