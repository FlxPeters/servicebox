<template>
  <b-container class="mt-4">
    <h1>Services</h1>
    <hr />
    <ServiceTable />
  </b-container>
</template>

<script>
import ServiceTable from "./ServiceTable.vue";
export default {
  name: "ServiceList",
  components: {
    ServiceTable,
  },
};
</script>
