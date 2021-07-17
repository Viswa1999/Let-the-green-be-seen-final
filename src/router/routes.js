const routes = [
  { 
     path: '/', component: () => import('layouts/MainLayout.vue') },
    { path: '/plant_trees', component: () => import('pages/Plant_Trees.vue') },
    { path: '/login', component: () => import('src/pages/Login.vue') },    
      { path: '/register', component: () => import('src/pages/Register.vue') },
      { path: '/new', component: () => import('src/pages/New.vue') },
      { path: '/plantneem', component: () => import('src/pages/PlantNeem.vue')},
      { path: '/plantvilvam', component: () => import('pages/PlantVilvam.vue')},
      { path: '/plantmango', component: () => import('pages/PlantMango.vue')},
      { path: '/whytoplanttrees', component: () => import('src/pages/WhyPlant.vue') },
      {path: '/donate', component: () => import('pages/Donate.vue'),

  children: [
    
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
