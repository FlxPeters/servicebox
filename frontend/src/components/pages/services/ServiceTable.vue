<template>
  <div>
    <b-table
      striped
      hover
      :items="services"
      :fields="fields"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
    >
      <template v-slot:cell(status)="data">
        <b-badge>{{ data.item.status }}</b-badge>
      </template>
      <template v-slot:cell(fqsn)="data">
        {{ data.item.owner.slug }}-{{ data.item.slug }}
      </template>

      <template v-slot:cell(actions)>
        Edit &middot; View
      </template>
    </b-table>
  </div>
</template>

<script>
const axios = require("axios").default;
export default {
  data() {
    return {
      sortBy: "name",
      sortDesc: false,
      fields: [
        "name",
        { key: "fqsn", label: "Full service name" },
        "status",
        { key: "owner.name", label: "Owner" },
        { key: "operator.name", label: "Operator" },
        { key: "platform.name", label: "Platform" },
        "actions",
      ],
      services: [],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/api/services/services/")
      .then((response) => {
        this.services = response.data;
      })
      .catch(function(error) {
        console.log(error);
      });
  },
};
</script>
