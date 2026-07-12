export default function LoginPage() {
    return (
        <main className="auth-page">
            <div className="auth-card">
                <h1>Sign In</h1>

                <form>
                    <input
                        type="text"
                        placeholder="Username"
                    />

                    <input
                        type="password"
                        placeholder="Password"
                    />

                    <button type="submit">
                        Sign In
                    </button>
                </form>
            </div>
        </main>
    );
}