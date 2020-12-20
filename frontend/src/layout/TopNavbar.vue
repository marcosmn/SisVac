<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">SUS - SisVac</a>
      <button
        type="button"
        class="navbar-toggler navbar-toggler-right"
        :class="{ toggled: $sidebar.showSidebar }"
        aria-controls="navigation-index"
        aria-expanded="false"
        aria-label="Toggle navigation"
        @click="toggleSidebar"
      >
        <span class="navbar-toggler-bar burger-lines"></span>
        <span class="navbar-toggler-bar burger-lines"></span>
        <span class="navbar-toggler-bar burger-lines"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end">
        <ul class="nav navbar-nav mr-auto">
          <li class="nav-item">
            <a href="#" class="nav-link"></a>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li v-if="logado" class="nav-item">
            <a class="nav-link" href="#" style="color:blue;">
              {{ nome }}
            </a>
          </li>
          <li v-if="!logado" class="nav-item">
            <a
              class="btn btn-block  btn-primary opcoes-login"
              href="#/user/login"
            >
              <span class="fa fa-sign-in"></span> <span>Login</span>
            </a>
          </li>
          <li v-if="logado" class="nav-item">
              <button type="submit" class="btn btn-primary" v-on:click="logout">
                Sair
              </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: mapState({
    routeName() {
      const { name } = this.$route;
      return this.capitalizeFirstLetter(name);
    },
    logado: (state) => state.userState.logado,
    nome: (state) => state.userState.nome,
  }),
  data() {
    return {
      activeNotifications: false,
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    ...mapActions("userState", ["getStatus","logout"]),
  },
  created() {
    this.$store.dispatch("userState/getStatus");
  },
};
</script>
<style></style>
