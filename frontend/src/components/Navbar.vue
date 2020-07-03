<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-container>
      <b-navbar-brand to="/">
        <img id="logo" height="30" src="../assets/img/logo_icon.svg" />
        ServiceBox
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"> </b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/services">Services</b-nav-item>
          <b-nav-item to="/platforms">Platforms</b-nav-item>
          <b-nav-item to="/tenants">Tenants</b-nav-item>
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
