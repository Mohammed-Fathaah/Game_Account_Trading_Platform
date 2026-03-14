import { BrowserRouter,Routes,Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Listings from "./pages/Listings";

function App(){
  return (
    <BrowserRouter>
     <Routes>
      <Route path="/" element={<Listings />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
     </Routes>
    </BrowserRouter>
  );
}

export default App