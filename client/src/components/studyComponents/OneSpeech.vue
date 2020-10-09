<template>
  <div>

    <div class="card" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
        <p class="card-text">
          Some quick example text to build on the card title
          and make up the bulk of the card's content.
        </p>
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </div>
    </div>

    <div class="card" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
        <p class="card-text">
          Some quick example text to build on the card title
          and make up the bulk of the card's content.
        </p>
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </div>
    </div>

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
      value: this.initalValue,
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
      'selectedSentence',
      'initalValue',
      'selectedSpeech',
      'sentenceSentiment',
      'speechLength',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchSpeechMean',
      'fetchSpeechSentenceSentiment',
    ]),
    submitForm(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.speech,
      };
      this.fetchSpeechMean({ payload });
    },
    changeSentence(direction) {
      let value = this.initalValue;
      if (direction === 'up') {
        value += 1;
      } else if (direction === 'down') {
        value -= 1;
      }
      if (value > this.speechLength) {
        alert('The end of the speech has been reached!');
      } else if (value < 0) {
        alert('You cannot go back any further');
      } else {
        const payload = {
          value,
          speech: this.selectedSpeech,
        };
        this.fetchSpeechSentenceSentiment({ payload });
      }
    },
  },
};
</script>

<style scoped>
#first-chart-area {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 3em;
  padding: 50px;
}

span {
  font-weight: bold;
}

.sentenceArea {
  height: 100px;
  width: 90%;
}

.svgLeft {
  margin-right: 10px;
}

.svgLeft:hover {
  color: red;
}

.svgRight:hover {
  color: red;
}

.average-sentiment-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
