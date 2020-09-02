<template>
  <div>
    <Navbar/>
    <h1>Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/view/Navbar.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
  },
};
</script>
