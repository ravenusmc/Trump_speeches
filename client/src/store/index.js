import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    oneSpeechChartData: [],
  },

  getters: {
  },

  actions: {

    // This action will get the data for the speech selected. Remember that
    // the action appears to NEED to take 2 arguments, not 1. 
    fetchOneSpeechChartData: ({ commit }, { payload }) => {
      console.log('In Action');
      console.log(payload.speech);
      const data = 'Mike';
      commit('setOneSpeechChartData', data);
      // const path = 'http://localhost:5000/routeOne';
      // axios.post(path, payload)
      // .then((res) => {
      //   res.data.sort((a, b) => b[1] - a[1]);
      //   commit('setFirstChartData', res.data);
      // });
    },

  },

  mutations: {

    setOneSpeechChartData(state, data) {
      state.oneSpeechChartData = data;
    },

  },

});
