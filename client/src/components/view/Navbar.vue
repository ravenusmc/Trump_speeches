<template>
  <div>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand"><router-link class='navbarTextColor' to="/">Trump Speeches
      </router-link></a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link"><router-link class='navbarTextColor' to="/">Home
            </router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link"><router-link class='navbarTextColor' to="/about">
              About</router-link></a>
          </li>
        </ul>
      </div>
</nav>

  </div>
</template>

<style>
.navbarTextColor {
  color: white;
}

.navbarTextColor:hover {
  color: red;
}
</style>
