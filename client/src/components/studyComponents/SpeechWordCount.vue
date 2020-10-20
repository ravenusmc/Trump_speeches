<template>
  <div>
    <h5 class='center'><span>Word Count for:</span> {{ this.selectedSpeech }}</h5>
    <GraphCard
     :typeOne='typeOne'
     :data='word_and_count_data'
     :options='chartOptionsOne'>
    </GraphCard>

  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/graphs/GraphCard.vue';

export default {
  name: 'SpeechWordCount',
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
        animation: {
          duration: 1000,
          easing: 'linear',
        },
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
      'selectedSpeech',
      'word_and_count_data',
    ]),
  }, // End Computed properties
};
</script>

<style scoped>
span {
  font-weight: bold;
}
</style>
