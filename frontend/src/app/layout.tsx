import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import styles from "./layout.module.css";

export const metadata: Metadata = {
  title: "Pet Profile",
  description: "Internal pet insurance profile management",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <header className={styles.header}>
          <div className={styles.headerInner}>
            <h1 className={styles.title}>
              <Link href="/" className={styles.titleLink}>
                Pet Profile
              </Link>
            </h1>
          </div>
        </header>
        <main className={styles.main}>
          <div className={styles.container}>{children}</div>
        </main>
      </body>
    </html>
  );
}
