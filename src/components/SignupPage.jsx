function SignupPage({ setPage, onSignup }) {
  return (
    <div className="auth-wrapper">
      <div className="auth-box">
        <h2>Signup</h2>

        <input placeholder="Full Name" />
        <input placeholder="Email" />
        <input type="password" placeholder="Password" />

        <button onClick={onSignup}>Create Account</button>

        <p style={{ marginTop: "12px" }}>
          Already have an account?{" "}
          <span
            style={{ color: "#2563eb", cursor: "pointer" }}
            onClick={() => setPage("login")}
          >
            Login
          </span>
        </p>
      </div>
    </div>
  );
}

export default SignupPage;
