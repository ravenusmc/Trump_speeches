<template>
  <div>
    <Navbar/>
    <Header/>
    <Background/>
    <OneSpeech/>
    <SentimentChart/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/view/Navbar.vue';
import Footer from '@/components/view/Footer.vue';
import Header from '@/components/home/Header.vue';
import OneSpeech from '@/components/studyComponents/OneSpeech.vue';
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
    Footer,
  },
};
</script>
