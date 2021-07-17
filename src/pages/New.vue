<template>
<div class="q-pa-md">
    <div class="q-gutter-sm row items-start">
      
     <!-- <q-form @submit="onSubmit"
      class="q-gutter-md"> -->
      <!-- <div v-if="isSuccess">Image Uploaded Successfully</div><br>
      <q-form class="q-gutter-md" action="">
      Upload Picture:<q-input v-modal="image" type="file" id="img" label="Image" /> -->
      <div v-if="isSuccess">Image successfully uploaded</div><br>
        <q-form action="">
             You can upload your picture here:<br><input type="file" id="img"><br>
            <br>
      <div>
        <q-btn color="grey-4" 
        @click.prevent="on_sumit" type="submit" text-color="purple" glossy unelevated icon="camera_enhance" label="Submit" />
      </div>
        </q-form><br>
      <!--q-uploader
        
        v-model="image"
        type="file"
        id="img"
        label="Batch upload"
        multiple
        batch
        style="max-width: 300px"
      /-->
      
      <div v-if="jobs.length">
    <div v-for="job in jobs" :key="job.id" class="job">
    <strong> </strong><br>
    <q-card class="my-card">
    <q-img :src="job.image" alt="" style="width:50%; height:50%"/><br>
    <strong>Your image is uploaded </strong><br>{{job.image}}
    </q-card>
    </div>
    </div>
      <!-- </q-form>  -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {api} from 'boot/axios'
export default{
  data() {
    return {
      image: '',
      caption: '',
      selectfile:"",
      isSuccess: false,
      'post_data': null,
      jobs:[],
      slide: 1,
    }
  },
   methods: {
    load_data() {
      api.get('http://127.0.0.1:8003/api/image/').then((resp) => {
          this.jobs = resp.data;
        })
    },
        on_sumit(){
            let form_data = new FormData();   //With this step, just upload files you do not need when you need to add additional fields 
            var img = document.getElementById('img').files[0];
            form_data.append('image',img,img.name);  // Here's image and backstage views view file name when you want to get, like, not otherwise get, see details below views view file
            axios({
                url:'http://127.0.0.1:8003/api/image/',
                method:'post',
                data:form_data,
                headers: {
                  'Content-Type': 'multipart/form-data'
                 }
            }).then((res) => {
        console.log(res);
        this.isSuccess=true
        this.info = res.statusText;
      }) 
      .catch((err)=>console.log(err.response.data));
        }
    },
    created() {
    this.load_data();
  } 
   /* methods: {
    load_data() {
      api.get('http://127.0.0.1:8000/api/image/')
      .then((resp) => {
          this.post_data = resp.data;
        })
    },
  },
  created() {
    this.load_data();
  }   */ 
  /* methods: {
  onSubmit() {
    axios.post("http://127.0.0.1:8000/api/image/media/img/21/")
    .then((resp)=>{
        console.log(resp);
      });
  } 
} */  
}
</script>

<style>

</style>