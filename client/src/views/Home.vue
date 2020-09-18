<template>
  <div>
    <Navbar/>
    <Header/>
    <Background/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/view/Navbar.vue';
import Footer from '@/components/view/Footer.vue';
import Header from '@/components/home/Header.vue';
import Background from '@/components/home/Background.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Header,
    Background,
    Footer,
  },
};
</script>
