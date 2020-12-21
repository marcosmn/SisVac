<template>
  <div class="wrapper">
    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/">
        <i class="nc-icon nc-bank"></i>
        <p>Home</p>
      </sidebar-link>
      <sidebar-link to="/user/cadastro">
        <i class="nc-icon nc-circle-09"></i>
        <p>Cadastro</p>
      </sidebar-link>
      <sidebar-link to="/vacina/agendar">
        <i class="nc-icon nc-single-copy-04"></i>
        <p>Agendar</p>
      </sidebar-link>
      <sidebar-link to="/user/carteira">
        <i class="nc-icon nc-credit-card"></i>
        <p>Carteira</p>
      </sidebar-link>
      <sidebar-link to="/vacina/fila">
        <i class="nc-icon nc-bell-55"></i>
        <p>Fila Espera</p>
      </sidebar-link>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <main-content @click="toggleSidebar">

      </main-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">

</style>
<script>
  import TopNavbar from './TopNavbar.vue'
  import ContentFooter from './ContentFooter.vue'
  import MainContent from './Content.vue'
  import MobileMenu from './MobileMenu.vue'
  export default {
    components: {
      TopNavbar,
      ContentFooter,
      MainContent,
      MobileMenu
    },
    methods: {
      toggleSidebar () {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }

</script>
