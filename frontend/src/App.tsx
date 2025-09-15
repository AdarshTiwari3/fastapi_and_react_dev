
import Component from '@/components' 

import {Routes, Route, BrowserRouter as Router} from 'react-router-dom'
import Hooks from '@/components/hooks';
function App() {
  return (
   <Router>
    <Routes>
      <Route path="/" element={<Component/>}/>
      <Route path='/route' element={<div className='bg-amber-800'>Hi Router</div>}/>
      <Route path='/hooks' element={<Hooks/>}/>
    </Routes>
   </Router>
  );
}

export default App;
