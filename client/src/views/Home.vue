<template>
  <div>

    <Navbar/>

    <section>
      <Header/>
      <Background/>
      <OneSpeech/>
      <SpeechWordCount/>
      <div class='center'>
        <button class="btn btn-outline-dark" v-on:click="say()">{{ this.buttonTitle }}</button>
      </div>
      <div v-if="showTrumpSpeeches">
        <SentimentChart/>
      </div>
      <div v-else>
        <SentimentChartObama/>
      </div>
    </section>

    <Footer/>

  </div>
</template>

<script>
import Navbar from '@/components/view/Navbar.vue';
import Footer from '@/components/view/Footer.vue';
import Header from '@/components/home/Header.vue';
import OneSpeech from '@/components/studyComponents/OneSpeech.vue';
import SpeechWordCount from '@/components/studyComponents/SpeechWordCount.vue';
import SentimentChart from '@/components/studyComponents/SentimentChart.vue';
import SentimentChartObama from '@/components/studyComponents/SentimentChartObama.vue';
import Background from '@/components/home/Background.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Header,
    Background,
    OneSpeech,
    SentimentChart,
    SentimentChartObama,
    SpeechWordCount,
    Footer,
  },
  data() {
    return {
      buttonTitle: 'Show Obama Speeches',
      showObamaSpeeches: false,
      showTrumpSpeeches: true,
    };
  },
  methods: {
    say() {
      if (this.showTrumpSpeeches === true) {
        this.buttonTitle = 'Show Trump Speeches';
        this.showObamaSpeeches = true;
        this.showTrumpSpeeches = false;
      } else if (this.showObamaSpeeches === true) {
        this.buttonTitle = 'Show Obama Speeches';
        this.showTrumpSpeeches = true;
        this.showObamaSpeeches = false;
      }
    },
  },
};
</script>

<style scoped>

section {
  margin-bottom: 50px;
}

</style>
