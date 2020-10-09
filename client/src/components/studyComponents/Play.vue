<section id='card'>

  <div class='card-body first-chart-area'>

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
      <p><span>Average Sentiment of Speech:</span> {{ this.speechMean }}</p>
    </form>
    <!-- End Boostrap Form -->
  </div>

  <div class='card-body'>
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
          <path fill-rule="evenodd" d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1
          0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0
          0-.708-.708L8.5 10.293V4.5z"/>
        </svg>
      </div>
    </div>
  </div>

</section>
