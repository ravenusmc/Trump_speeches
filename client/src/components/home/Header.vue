<template>
  <div>
    <header>
      <div>
        <h1>Trump Speeches</h1>
      </div>
    </header>
  </div>
</template>

<script>

export default {
  name: 'Header',
};

</script>

<style scoped>

header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url('../../assets/images/trump_speech.jpeg');
  height: 675px;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

header div {
  padding: 20px;
  color: red;
  background-color: rgba(52, 58, 64, 0.8);
}
</style>
