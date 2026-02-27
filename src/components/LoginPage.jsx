function LoginPage({ setPage, onLogin }) {
  return (
    <div className="auth-wrapper">
      <div className="auth-box">
        <h2>Login</h2>

        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />

        <button onClick={onLogin}>Login</button>

        <p style={{ marginTop: "12px" }}>
          New user?{" "}
          <span
            style={{ color: "#2563eb", cursor: "pointer" }}
            onClick={() => setPage("signup")}
          >
            Signup here
          </span>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
