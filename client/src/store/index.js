import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    oneSpeechChartData: [],
    speechMean: 0.11,
    initialSentence: 'Thank you very much.',
    initalValue: 0,
  },

  getters: {
    speechMean: (state) => state.speechMean,
    initialSentence: (state) => state.initialSentence,
    initalValue: (state) => state.initalValue,
  },

  actions: {

    // This action will get the data for the speech selected. Remember that
    // the action appears to NEED to take 2 arguments, not 1.
    fetchSpeechMean: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/get_sentiment_by_speech';
      axios.post(path, payload)
        .then((res) => {
          commit('setSpeechMean', res.data);
        });
    },
    // This action will get the sentiment of a single sentence based on a speech.
    fetchSpeechSentenceSentiment: ({ commit }, { payload }) => {
      console.log('In Action');
      console.log(payload);
      commit('setInitialSentence', 'Hi');
      // const path = 'http://localhost:5000/get_sentiment_by_speech';
      // axios.post(path, payload)
      //   .then((res) => {
      //     console.log(res.data);
      //     commit('setSpeechMean', res.data);
      //   });
    },

  },

  // res.data.sort((a, b) => b[1] - a[1]);

  mutations: {

    setSpeechMean(state, data) {
      state.speechMean = data;
    },

    setInitialSentence(state, data) {
      state.initialSentence = data;
    },

  },

});
