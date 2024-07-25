import { createStore } from 'vuex'

export default createStore({
  state: {
    rooms:{},
    data:{}
  },
  getters: {
  },
  mutations: {
    ADD_TO_ROOMS: (state, items) => {
      state.rooms = items
    },
    ADD_TO_DATA: (state, items) => {
      state.data = items
    },

  },
  actions: {
  },
  modules: {
  }
})
