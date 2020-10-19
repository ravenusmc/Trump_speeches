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
    word_and_count_data: [
      ['Word', 'Count'],
      ['working', 10],
      ['money', 10],
      ['good', 10],
      ['framework', 10],
      ['america', 10],
      ['country', 11],
      ['companies', 11],
      ['great', 15],
      ['taxes', 15],
      ['businesses', 15],
      ['people', 16],
      ['jobs', 17],
      ['right', 18],
      ['their', 19],
      ['american', 30],
      ['you', 44],
      ['they', 47],
      ['tax', 60],
      ['our', 78],
      ['we', 103],
    ],
    allSpeechesSentiment: [
      ['Speech_Title', 'Sentiment'],
      ["Trump's Remarks On Iran Nuclear Deal", 0.03356339164844319],
      ['Remarks by the President in Nashville, Tennessee', 0.06784631958331197],
      ['President Trump addressed the nation on Monday from Fort Myer military base in Arlington, Va., to lay out his military plans for Afghanistan.', 0.08150194547515976],
      ['Remarks at the Conservative Political Action Conference in National Harbor, Maryland', 0.0817595852055201],
      ["Trump's speech in Warsaw", 0.09119367868227801],
      ['President Trumps Address to a Joint Session of Congress', 0.09185193857378847],
      ['America First, security speech at the Ronald Reagan Building', 0.0919181993655499],
      ['Trump Declares Opioid Crisis a Public Health Emergency', 0.09254466966966966],
      ['News Conference with Prime Minister Netanyahu of Israel', 0.09624651188140398],
      ['Remarks by President Trump on TaxReform', 0.09887185400128176],
      ['Phoenix Arizona Rally Speech', 0.10226042145249743],
      ['Remarks by President Trump at Tax Reform Event', 0.10832021401050984],
      ['President Trump on the Paris Climate Accord', 0.11247572435696192],
      ['Remarks at the National Rifle Association Leadership Forum in Atlanta, Georgia', 0.12596520373271342],
      ['inauguration speech', 0.1270178391053391],
      ['Remarks by the President at the NRCC Dinner', 0.12740312991726302],
      ['Remarks at the Central Intelligence Agency', 0.1291384869099155],
      ['Remarks at a Make America Great Again Rally in Melbourne Florida', 0.13552409554383238],
      ['2017 Boy Scout Jamboree Speech', 0.17546965803625636],
      ["Remarks With Prime Minister Enda Kenny of Ireland at a St. Patrick's Day Reception", 0.2061718348523904],
    ],
    ObamaSpeechesSentiment: [
      ['Speech_Title', 'Sentiment'],
      ['Remarks at the Conservative Political Action Conference in National Harbor, Maryland', 0.10386522967772965],
      ['Speech to the American Medical Association', 0.1065579509379509],
      ['First Press Statement on the Attempted Christmas Day Terrorist Bombing Attack in Detroit', 0.1299366304554984],
      ['Speech on 2010 Budget Sent to Congress', 0.08737279883621349],
      ['Tribal Nations Conference Address', 0.12084064208392173],
      ['Statement on the Sandy Hook Elementary School Shootings in Newtown, Connecticut', 0.15808531746031745],
      ['Address to the People of Northern Ireland', 0.10619824863857524],
      ['Statement on Afghanistan', 0.12205013384361209],
      ['Address on Iran at American University', 0.07702010747105681],
      ['Afghanistan Troop Reduction Address to the Nation', 0.07917152006069532]
    ]
  },

  getters: {
    speechMean: (state) => state.speechMean,
    selectedSentence: (state) => state.selectedSentence,
    initalValue: (state) => state.initalValue,
    selectedSpeech: (state) => state.selectedSpeech,
    sentenceSentiment: (state) => state.sentenceSentiment,
    speechLength: (state) => state.speechLength,
    allSpeechesSentiment: (state) => state.allSpeechesSentiment,
    word_and_count_data: (state) => state.word_and_count_data,
  },

  actions: {

    fireActions: ({ dispatch }, { payload }) => {
      dispatch('fetchSpeechMean', { payload });
      dispatch('fetchWordCount', { payload });
    },

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

    fetchWordCount: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/fetch_word_count';
      axios.post(path, payload)
        .then((res) => {
          res.data.sort((a, b) => a[1] - b[1]);
          commit('setWordAndCountData', res.data);
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

    setWordAndCountData(state, data) {
      state.word_and_count_data = data;
    },

  },

});
