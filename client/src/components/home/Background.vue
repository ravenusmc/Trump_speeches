<template>
  <div>

    <div class='title-area'>
      <h1 class='center'>Background</h1>
    </div>

    <section>

        <div>
          <p>
            Back in the spring of 2018, I first heard about Natural Language
            Processing from a Teacher at Gwinnett Technical College located outside
            of Atlanta. It really caught my attention and I almost immediately
            wanted to learn more about it. I decided to make a project examining
            the sentiment of tweets about Trump. I used a simple NLP program called
            textBlob, which this project also uses. Eventually, one day, I'll get
            into using NLTK. From that first Twitter project I've made numerous
            projects using NLP. This is one of them and it won't be the last.
          </p>
        </div>

        <div>
          <p>
            This project is focusing on about twenty speeches that I have that Trump
            gave throughout his time as President. The goal is to see the average
            sentiment of each speech as well as the common words in them. To get the
            average sentiment, I get the sentiment of a single sentence and then take
            the mean of all the sentences together. I next look at the most common
            words in his speeches to see what they show - if anything at all.
          </p>
        </div>

    </section>
  </div>
</template>

<script>
export default {
  name: 'Background',
};
</script>

<style scoped>

.title-area {
  margin-top: 50px;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 50px 5% 50px 5%;
}

section div {
  margin: 0 5px 0 5px;
}

@media only all and (max-width: 1000px) {

  section {
  grid-template-columns: 1fr;
  margin: 50px 5% 50px 5%;
  }

}

</style>
