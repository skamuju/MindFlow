import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Mindflow",
  description: "Created by a team of UCSD students to help users navigate and manage their mental health through assisted journaling",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
