const express = require('express');
const { registerUser, loginUser,getusers } = require('../controllers/Usercontroller');

const router = express.Router();

router.post('/register', registerUser);
router.post('/login', loginUser);
router.get('./all',getusers);

module.exports = router;
