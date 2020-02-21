import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.TimeUnit;

import static java.time.temporal.ChronoUnit.SECONDS;

// Program to calculate execution time or elapsed time in Java
class Main
{
	public static void main(String[] args) throws InterruptedException {

		Instant start = Instant.now();
		// ... the code being measured starts ...

		// sleep for 5 seconds
		TimeUnit.SECONDS.sleep(5);

		// ... the code being measured ends ...

		Instant end = Instant.now();

		Duration interval = Duration.between(start, end);

		System.out.println("Execution time in seconds: " + interval.getSeconds());
		System.out.println("Execution time in seconds: " + interval.get(SECONDS));
	}
}