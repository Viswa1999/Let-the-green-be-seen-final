<template>
  <div class="q-pa-md" style="max-width: 400px">
    <div v-if="isSuccess"><router-link :to="'../src/pages/Register.vue'"></router-link></div>
    <q-form
      @submit.prevent="addNote"
      class="q-gutter-md"
    >
    {{post_data}}
    <div v-if="error">{{error}}</div>
    <div v-if="isSuccess">Logged in </div>
      <q-input
        filled
        type="email"
        v-model="email"
        label="Your email *"
        hint="Name and surname"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type something']"
      />

      <q-input
        filled
        type="password"
        v-model="password"
        label="Your password *"
        hint="Name and surname"
        lazy-rules
        :rules="[ val => val && val.length > 0 && val.length < 10 || 'Please type something']"
      />

      <div>
        <q-btn label="Submit" type="submit" color="primary"></q-btn>
        <!--q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" /-->
        <q-btn><router-link to="/register">Already a member</router-link></q-btn>
      </div>
    </q-form>
  </div>
  <div v-if="jobs.length">
    <div v-for="job in jobs" :key="job.password" class="job">
    <strong>Your image is uploaded in this url </strong>"{{job.email}}"{{job.password}}
    </div>
    </div>
    {{post_data}}
    
    
</template>

<script>
import axios from 'axios'
import { api } from 'boot/axios'
//import { useQuasar } from 'quasar'
//import { ref } from 'vue'

export default {
  
  data() {
    return {
      email:'',
      password:'',
      isSuccess: false,
      'post_data':null,
      jobs:[],
      error:null,
    }
  },
  methods: {
    load_data() {
      axios.get('http://127.0.0.1:8000/api/tasks/').then((resp) => {
          this.post_data = resp.data;
        })
    },
    addNote:async function () {
      const auth = {email:this.email,password:this.password};
      const url = 'http://127.0.0.1:8000/api/tasks/';
      this.isSuccess = false;
      this.error=null;
      try {
        const res = await axios.get(url,{auth})
        .then(res => res.data);
        this.isSuccess=true;
      } catch (err) {
        this.error=err.message;
      }
     /* {
      api.post('http://127.0.0.1:8000/api/tasks/',
      {fname:this.fname,lname:this.lname,email:this.email,password:this.password,repassword:this.repassword},)
      .then((resp)=>{
        this.isSuccess=true;
        console.log(resp);
        this.$router.push('/');
      });
    }, */
  },
  created() {
    this.load_data();
  }
  /*data() {
    return {
      fname:'',
      lname:'',
      email:'',
      password:'',
      repassword:'',
      isSuccess: false,
      'post_data':[],
    }
  },
  methods: {
    load_data() {
        axios.get('http://localhost:8000/api/tasks/')
        .then((resp) => {
          this.post_data = resp.data;
        })
      },
      addNote() {
        axios.post('http://localhost:8000/api/tasks/',
        {fname:this.fname,lname:this.lname,email:this.email,password:this.password,repassword:this.repassword},)
        .then((resp)=> {
          this.isSuccess = true;
          console.log(resp);
          //this.post_data = resp.data;
        });
      },
    },
    created() {
      this.load_data();
    }*/

  /*setup () {
    const $q = useQuasar()

    const fname = ref(null)
    const lname = ref(null)
    const fnameRef = ref(true)
    const lnameRef = ref(true)

    const email = ref(null)
    const emailRef = ref(true)

    const password = ref(null)
    const passRef = ref(true)

    const repassword = ref(null)
    const repassRef = ref(true)

    const accept = ref(false)
  
    return {
      text: ref(''),
      fname,
      lname,
      nameRules: [
        val => (val && val.length > 0) || 'Please type your name'
      ],

      email,
      emailRef,
      emailRules: [
        val => (val !== null && val !== '') || 'Please type your email',
        //val => (val > 0 && val < 100) || 'Please type a real age'
      ],

      password,
      passRef,
      passwordRules: [
        val => (val !== null && val !== '') || 'Please type your password',
      ],

      repassword,
      repassRef,
      repasswordRules: [
        val => (val !== null && val !== '') || 'Please type your password',
      ],
      accept,
      isSuccess:false,
      addNote () {
        

        axios.post('http://127.0.0.1:8000/api/tasks/',
        {fname:this.fname,lname:this.lname,email:this.email,password:this.password,repassword:this.repassword},)
        .then((resp)=> {
          this.isSuccess = true;
          console.log(resp);
        });

        if (fnameRef.value.hasError || lnameRef.value.hasError || emailRef.value.hasError || passRef.value.hasError || repassRef.value.hasError) {
          // form has error
        }
        else if (accept.value !== true) {
          $q.notify({
            color: 'negative',
            message: 'You need to accept the license and terms first'
          })
        }
        
      },

      onReset () {
        fname.value = null
        lname.value = null
        email.value = null
        password.value = null
        repassword.value = null

        fnameRef.value.resetValidation()
        lnameRef.value.resetValidation()
        emailRef.value.resetValidation()
        passRef.value.resetValidation()
        repassRef.value.resetValidation()
      }
    }
  },*/

  //methods: {
    /*addNote() {
        axios.post('http://localhost:8000/api/tasks/',
        {title:this.title,content:this.content},)
        .then((resp)=> {
          this.isSuccess = true;
          console.log(resp);
        });
      },*/

    /*onReset () {
      this.name = null
      this.age = null
      this.accept = false
    }*/
  //}
  
  },
}
</script>

<style style="scss" scoped>
.my-custom-image{
  filter: blur(1px) sepia();
}

</style>
