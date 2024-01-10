<template>
  <section>
    <p>This site is built with FastAPI and Vue.</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all employees.</p>
    </div>
    <p v-else>
      <div @click="c">
        hersd
      </div>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    c() {
      console.log(this.$store.getters.stateUser)
    }
  }
});
</script>