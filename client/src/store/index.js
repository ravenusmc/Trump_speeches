import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    oneSpeechChartData: [],
    speechMean: 0.11,
    selectedSentence: 'Thank you very much.',
    initalValue: 0,
    selectedSpeech: 'Remarks by President Trump at Tax Reform Event',
    sentenceSentiment: 0,
    speechLength: 303, // Speech length for initial speech
  },

  getters: {
    speechMean: (state) => state.speechMean,
    selectedSentence: (state) => state.selectedSentence,
    initalValue: (state) => state.initalValue,
    selectedSpeech: (state) => state.selectedSpeech,
    sentenceSentiment: (state) => state.sentenceSentiment,
    speechLength: (state) => state.speechLength,
  },

  actions: {

    // This action will get the data for the speech selected. Remember that
    // the action appears to NEED to take 2 arguments, not 1.
    fetchSpeechMean: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/get_sentiment_by_speech';
      axios.post(path, payload)
        .then((res) => {
          const initialValue = 0;
          commit('setSpeechMean', res.data[0]);
          commit('setSpeechLength', res.data[1]);
          commit('setInitialSpeeh', payload.speech);
          commit('setInitialValue', initialValue);
        });
    },
    // This action will get the sentiment of a single sentence based on a speech.
    fetchSpeechSentenceSentiment: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/fetch_speech_sentence_sentiment';
      axios.post(path, payload)
        .then((res) => {
          commit('setSelectedSentence', res.data[0]);
          commit('setSentenceSentiment', res.data[1]);
          commit('setInitialValue', payload.value);
        });
    },

  },

  // res.data.sort((a, b) => b[1] - a[1]);

  mutations: {

    setSpeechMean(state, data) {
      state.speechMean = data;
    },

    setSelectedSentence(state, data) {
      state.selectedSentence = data;
    },

    setInitialValue(state, data) {
      state.initalValue = data;
    },

    setInitialSpeeh(state, data) {
      state.selectedSpeech = data;
    },

    setSentenceSentiment(state, data) {
      state.sentenceSentiment = data;
    },

    setSpeechLength(state, data) {
      state.speechLength = data;
    },

  },

});
