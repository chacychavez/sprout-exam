<template>
  <div v-if="regularEmployee">
    <p><strong>First name:</strong> {{ regularEmployee.first_name }}</p>
    <p><strong>Last name:</strong> {{ regularEmployee.last_name }}</p>
    <p><strong>Email:</strong> {{ regularEmployee.email }}</p>
    <p><strong>Number of leaves:</strong> {{ regularEmployee.number_of_leaves }}</p>
    <p><strong>Benefits:</strong> {{ regularEmployee.benefits }}</p>

    <div >
      <p><router-link :to="{name: 'EditEmployee', params:{type: 'Regular', id: regularEmployee.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeRegularEmployee()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
  <div v-if="contractualEmployee">
    <p><strong>First name:</strong> {{ contractualEmployee.first_name }}</p>
    <p><strong>Last name:</strong> {{ contractualEmployee.last_name }}</p>
    <p><strong>Email:</strong> {{ contractualEmployee.email }}</p>
    <p><strong>Contract end date:</strong> {{ contractualEmployee.contract_end_date }}</p>
    <p><strong>Projects:</strong> {{ contractualEmployee.projects }}</p>
    <div >
      <p><router-link :to="{name: 'EditEmployee', params:{type: 'Contractual', id: contractualEmployee.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeC()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>
  
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Employee',
  props: ['type', 'id'],
  async created() {
    try {
      
      if (this.type ==='Regular')
        await this.viewRegularEmployee(this.id);
      else 
        await this.viewContractualEmployee(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ regularEmployee: 'stateRegularEmployee', contractualEmployee: 'stateContractualEmployee'}),
  },
  methods: {
    ...mapActions(['viewRegularEmployee', 'viewContractualEmployee', 'deleteRegularEmployee', 'deleteContractualEmployee']),
    async removeEmployee() {
      try {
        if(this.type === 'Regular') 
          await this.deleteRegularEmployee(this.id);
        else
          await this.deleteContractualEmployee(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>