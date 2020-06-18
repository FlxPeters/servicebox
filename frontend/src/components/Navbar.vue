<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-container>
      <b-navbar-brand href="#">
        <img id="logo" height="30" src="../assets/img/logo_icon.svg" />
        ServiceBox
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"> </b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Services</b-nav-item>
          <b-nav-item href="#">Platforms</b-nav-item>
          <b-nav-item href="#">Tenants</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
