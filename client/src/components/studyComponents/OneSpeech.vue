<template>
  <div>

    <section id='first-data-area'>

      <!-- <div class="card" style="width: 35rem;"> -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title center">Sentiment of a Speech</h5>
          <!-- Bootstrap From  -->
          <form @submit="submitForm">
            <div class="form-group">
              <label for="exampleInputEmail1"><span>Select Speech:</span></label>
              <select class="custom-select" v-model="speech" name="speech">
                <option v-for="speech in speeches" v-bind:key="speech" :value="speech">
                  {{ speech }}
                </option>
              </select>
            </div>
            <button type="submit" class="btn btn-outline-dark">Submit</button>
            <p><span>Selected Speech:</span> {{ this.selectedSpeech }}</p>
            <p><span>Average Sentiment of Speech:</span> {{ this.speechMean }}</p>
          </form>
          <!-- End Boostrap Form -->
        </div>
      </div>

      <!-- <div class="card" style="width: 35rem;"> -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title center">Sentence Sentiment</h5>
          <div class='average-sentiment-div'>
            <div class='sentenceArea'>
              <p><span>Current Sentence:</span> {{ this.selectedSentence }}</p>
            </div>
            <p>Sentence Sentiment: {{ this.sentenceSentiment }}</p>
            <h4>Change Sentence:</h4>
            <div>
              <svg
              @click="changeSentence('up')"
              width="3em"
              height="3em"
              viewBox="0 0 16 16"
              class="bi bi-arrow-up-circle-fill svgLeft"
              fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354
                7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5
                5.707V11.5z"/>
              </svg>
              <svg @click="changeSentence('down')" width="3em" height="3em" viewBox="0 0 16 16"
                class="bi bi-arrow-down-circle-fill svgRight"
                fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5
                4.5a.5.5 0 0 0-1
                0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0
                0-.708-.708L8.5 10.293V4.5z"/>
              </svg>
            </div>
          </div>
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
      'fireActions',
      'fetchSpeechSentenceSentiment',
    ]),
    submitForm(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.speech,
      };
      this.fireActions({ payload });
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
#first-data-area {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 3em;
  padding: 50px;
}

span {
  font-weight: bold;
}

.sentenceArea {
  height: 150px;
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

@media only all and (max-width: 1500px) {

  .card {
    width: 35rem;
  }

}

@media only all and (max-width: 1200px) {

  .card {
    width: 30rem;
  }

}

@media only all and (max-width: 1030px) {

  #first-data-area {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .card {
    width: 25rem;
  }

}

</style>
