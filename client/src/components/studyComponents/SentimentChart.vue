<template>
  <div>
    <GraphCard
     :typeOne='typeOne'
     :data='allSpeechesSentiment'
     :options='chartOptionsOne'>
    </GraphCard>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/graphs/GraphCard.vue';

export default {
  name: 'SentimentChart',
  components: {
    GraphCard,
  },
  data() {
    return {
      typeOne: 'ColumnChart',
      chartOptionsOne: {
        title: 'Word Count',
        legend: { position: 'top' },
        colors: ['#333'],
        height: 600,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
  computed: {
    ...mapGetters([
      'allSpeechesSentiment',
    ]),
  }, // End Computed properties
};
</script>

<style scoped>
</style>
