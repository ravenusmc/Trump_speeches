<template>
  <div>

    <Navbar/>

    <section>
      <Header/>
      <Background/>
      <OneSpeech/>
      <SpeechWordCount/>
      <button v-on:click="say()">{{ this.buttonTitle }}</button>
      <div v-if="showTrumpSpeeches">
        <SentimentChart/>
      </div>
      <div v-else>
        Now you don't
      </div>
    </section>

    <Footer/>

  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/view/Navbar.vue';
import Footer from '@/components/view/Footer.vue';
import Header from '@/components/home/Header.vue';
import OneSpeech from '@/components/studyComponents/OneSpeech.vue';
import SpeechWordCount from '@/components/studyComponents/SpeechWordCount.vue';
import SentimentChart from '@/components/studyComponents/SentimentChart.vue';
import Background from '@/components/home/Background.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Header,
    Background,
    OneSpeech,
    SentimentChart,
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
