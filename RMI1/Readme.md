New Terminal 1 [Dont close!]

$ touch Hello.java
$ touch HelloClient.java
$ touch HelloInterface.java
$ java HelloServer.java

error:
HelloServer.java:10: error: cannot find symbol

$ javac *.java
$ java HelloServer.java
error: class found on application class path: HelloServer

$ rmiregistry




Server Side: Open New Terminal 2 [Dont close!]

$ java HelloServer

Output: Hello Server is ready.




Client Side: Open New Terminal 3 [Dont close!]

$ java HelloClient

Output: Hello, world!

