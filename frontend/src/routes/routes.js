import MainLayout from '../layout/MainLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Home from 'src/pages/Home.vue'
import Login from 'src/pages/Login.vue'
import UserProfile from 'src/pages/UserProfile.vue'
import Carteira from 'src/pages/Carteira.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '/',
        name: 'home',
        component: Home,
      },
      {
        path: '/user/login',
        name: 'login',
        component: Login,
      },
      {
        path: '/user/cadastro',
        name: 'cadastro',
        component: UserProfile,
      },
      {
        path: '/user/carteira',
        name: 'carteria',
        component: Carteira,
      }
    ]
  },
 
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes
