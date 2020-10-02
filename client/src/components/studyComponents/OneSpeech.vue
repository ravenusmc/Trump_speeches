<template>
  <div>
    <section id='first-chart-area'>
      <div>
        <!-- Bootstrap From -->
        <form @submit="submitForm">
          <div class="form-group">
            <label for="exampleInputEmail1">Select Speech:</label>
            <select class="custom-select" v-model="speech" name="speech">
              <option v-for="speech in speeches" v-bind:key="speech" :value="speech">
                {{ speech }}
              </option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <!-- End Boostrap Form -->
      </div>
      <div>
        <div class='average-sentiment-div'>
          <p><span>Average Sentiment in Speech:</span> {{ this.speechMean }}</p>
          <p>Current Sentence: </p>
          <p>Sentence Sentiment: </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'OneSpeech',
  components: {
  },
  data() {
    return {
      speech: 'Remarks by President Trump at Tax Reform Event',
      speeches: [
        'Remarks by President Trump on TaxReform',
        'President Trumps Address to a Joint Session of Congress',
        'President Trump on the Paris Climate Accord',
        'Remarks by the President at the NRCC Dinner',
        'Remarks by the President in Nashville, Tennessee',
        '2017 Boy Scout Jamboree Speech', 'Phoenix Arizona Rally Speech',
        "Trump's Remarks On Iran Nuclear Deal",
        'President Trump addressed the nation on Monday from Fort Myer military base in Arlington, Va., to lay out his military plans for Afghanistan.',
        'America First, security speech at the Ronald Reagan Building',
        "Trump's speech in Warsaw", 'inauguration speech',
        'Trump Declares Opioid Crisis a Public Health Emergency',
        'Remarks by President Trump at Tax Reform Event', 'Remarks at the Central Intelligence Agency',
        'News Conference with Prime Minister Netanyahu of Israel',
        'Remarks at a Make America Great Again Rally in Melbourne Florida',
        'Remarks at the Conservative Political Action Conference in National Harbor, Maryland',
        "Remarks With Prime Minister Enda Kenny of Ireland at a St. Patrick's Day Reception",
        'Remarks at the National Rifle Association Leadership Forum in Atlanta, Georgia',
      ],
    };
  },
  computed: {
    ...mapGetters([
      'speechMean',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchSpeechMean',
    ]),
    submitForm(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.speech,
      };
      this.fetchSpeechMean({ payload });
    },
  },
};
</script>

<style scoped>
#first-chart-area {
  border: 2px solid red;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 3em;
}

span {
  font-weight: bold;
}

.average-sentiment-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
